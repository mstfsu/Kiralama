$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});
$(document).ready(function() {
    var $crf_token = $('#csrf_token').attr('value');
    $('#createIhaForm').submit(function(e) { // catch the form's submit event
        e.preventDefault();
        var formData = new FormData($(this)[0]);
        var categoryList = $('.category-multiple').val().map(function(item) {
            return parseInt(item);
        });
        formData.set('category', categoryList);
        //formData.append('image', $('#image')[0].files[0]);
        if (!$("#createIhaForm").valid()) {
            return;
        }
        $.ajax({ // create an AJAX call...
            data: formData, // get the form data
            type: "POST", // GET or POST
            url: "/iha/",
            processData: false,
            contentType: false,
            enctype: 'multipart/form-data',
            headers: {
                "X-CSRFToken": $crf_token,

            },
            success: function(response) {
                Swal.fire(
                    'Tebrikler!',
                    'IHA oluşturuldu!',
                    'success'
                )
                window.location.href = "/index";
            },error: function(response) {
                Swal.fire(
                    'Hata!',
                    response.statusText ,
                    'error'
                )
            }
        });
        return false;
    });
    $('.category-multiple').select2({
        allowClear: true,
        placeholder: "Kategori Seçiniz",
        width: '100%',
        ajax: {
            url: "/iha/category/",
            dataType: 'json',
            type: "GET",
            delay: 250,
            data: function(params) {
                return {
                    name__icontains: params.term
                };
            },
            error: function(data) {
                //can be used to log error
                console.log('Error:', data);
            },
            processResults: function(data) {
                return {
                    results: $.map(data.results, function(item) {
                        return {
                            text: item.name,
                            id: item.id
                        }
                    })
                };
            },
            cache: true
        }
    });

    $('.brand-multiple').select2({
        allowClear: true,
        placeholder: "Brand Seçiniz",
        width: '100%',
        ajax: {
            url: "/iha/brand/",
            dataType: 'json',
            type: "GET",
            delay: 250,
            data: function(params) {
                return {
                    name__icontains: params.term
                };
            },
            error: function(data) {
                //can be used to log error
                console.log('Error:', data);
            },
            processResults: function(data) {
                return {
                    results: $.map(data.results, function(item) {
                        return {
                            text: item.name,
                            id: item.id
                        }
                    })
                };
            },
            cache: true
        }
    });

    $("#createIhaForm").validate({
        errorClass: "input-error-class",
        validClass: "input-valid-class",
        rules: {
            name: {
                required: true,
            },
            model_number: {
                required: true,
            },
            description: {
                required: true,
            },
            category: {
                required: true,
            },
            brand: {
                required: true,
            },
            weight: {
                required: true,
            },
        },
        debug: true,
    });
});