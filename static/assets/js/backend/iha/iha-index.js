var $crf_token = $('#csrf_token').attr('value');
function deleteIHA() {
    var id = $("#deletedId").val();
    $.ajax({
        url: '/iha/' + id + '/ ',
        type: 'DELETE',
        headers: {
            "X-CSRFToken": $crf_token
        },
        success: function (result) {
            $('#deleteModal').modal('hide');
            $('#ourtable2').DataTable().ajax.reload();
        },
        error: function (data) {
            //can be used to log error
            console.log('Error:', data);
        },
    });
}
$(".custom-file-input").on("change", function () {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});
$(document).ready(function () {
    //md.initDashboardPageCharts();
    $('.categoryFilter').select2({
        allowClear: true,
        placeholder: "Filtrelemek için Kategori Seçiniz",
        ajax: {
            url: "/iha/category/",
            dataType: 'json',
            type: "GET",
            delay: 250,
            data: function (params) {
                return {
                    name__icontains: params.term
                };
            },
            error: function (data) {
                //can be used to log error
                console.log('Error:', data);
            },
            processResults: function (data) {
                return {
                    results: $.map(data.results, function (item) {
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
    $('#editIhaForm').submit(function (e) { // catch the form's submit event
        e.preventDefault();
        var formData = new FormData($(this)[0]);
        var categoryList = $('.category-multiple').val().map(function (item) {
            return parseInt(item);
        });
        formData.set('category', categoryList);
        //update the form data and send it via ajax
        $.ajax({ // create an AJAX call...
            data: formData, // get the form data
            type: "PUT", 
            url: "/iha/" + $("#editId").val() + "/",
            processData: false,
            contentType: false,
            enctype: 'multipart/form-data',
            headers: {
                "X-CSRFToken": $crf_token,

            },
            success: function (response) {
                Swal.fire(
                    'Tebrikler!',
                    'IHA Düzenlendi!',
                    'success'
                )
                $('#ourtable2').DataTable().ajax.reload();
                $('#editModal').modal('hide');
            }, error: function (response) {
                Swal.fire(
                    'Hata!',
                    response.statusText,
                    'error'
                )
            }
        });
        return false;
    });
    $(document).on('click', '.deleteButton', function (event) {
        event.preventDefault();
        $("#deletedId").val($(this).attr('data-id'));
        $('#deleteModal').modal('show');
    });

    $(document).on('click', '.editButton', function (event) {
        event.preventDefault();
        var ihaId = $(this).attr('data-id');
        $("#editId").val(ihaId);
        $.ajax({
            url: '/iha/' + ihaId + '/ ',
            type: 'GET',
            headers: {
                "X-CSRFToken": $crf_token
            },
            success: function (result) {
                $('#editModal').modal('show');
                $('[name="name"]').val(result.name);
                $('[name="model_number"]').val(result.model_number);
                $('[name="brand"]').val(result.brand.id).trigger('change');
                $('[name="weight"]').val(result.weight);
                $('[name="description"]').val(result.description);
                var category = result.category.map(function (item) {
                    return item.id;
                });
                $('[name="category"]').val(category).trigger('change');

            },
            error: function (data) {
                //can be used to log error
                console.log('Error:', data);
            },
        });
    });

    var table = $('#ourtable2').DataTable({
        serverSide: true,
        searching: true,
        processing: true,
        "ajax": {
            url: "/iha/?format=datatables",
            type: "GET",
            data: function (d) {
                d.category = $('.categoryFilter').val();
            },
            error: function (data) {
                //can be used to log error
                console.log('Error:', data);
            },
        },
        "columns": [{
            data: "image",
            name: "image",
            searchable: false,
            orderable: false,
            render: function (data, type, row) {
                return (
                    '<img src="' +
                    data +
                    '" width="100px" height="100px" />'
                );
            }
        },
        {
            data: "name",
            name: "name",
            searchable: true,
        },
        {
            data: "model_number",
            name: "model_number",
            searchable: true,
            orderable: false,

        },
        {
            data: "brand.name",
            name: "brand.name",
            searchable: true,
            orderable: true,
        },
        {
            data: "category",
            name: "category",
            searchable: false,
            orderable: false,
            render: function (data, type, row) {
                return data.map(function (item) {
                    return item.name;
                });
            }
        },
        {
            data: "weight",
            name: "weight",
            searchable: true,
            orderable: true,

        },
        {
            data: "description",
            name: "description",
            searchable: true,
            orderable: true,
        },
        {
            data: "actions",
            name: "actions",
            searchable: false,
            orderable: false,
            render: function (data, type, row) {
                return (
                    '<a href="#" class="btn btn-primary btn-sm editButton" data-id=' + row.id + '>Edit</a> <a href="#" data-id=' +
                    row.id +
                    ' class="btn btn-danger btn-sm deleteButton">Delete</a>'
                );
            }
        },
        ],
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
            data: function (params) {
                return {
                    name__icontains: params.term
                };
            },
            error: function (data) {
                //can be used to log error
                console.log('Error:', data);
            },
            processResults: function (data) {
                return {
                    results: $.map(data.results, function (item) {
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
            data: function (params) {
                return {
                    name__icontains: params.term
                };
            },
            error: function (data) {
                //can be used to log error
                console.log('Error:', data);
            },
            processResults: function (data) {
                return {
                    results: $.map(data.results, function (item) {
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
    $('.categoryFilter').on("select2:select", function (e) {
        table.draw();
    });
    $('.categoryFilter').on("select2:unselect", function (e) {
        table.draw();
    });

});