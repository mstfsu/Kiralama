var $crf_token = $('#csrf_token').attr('value');
function deleteCategory() {
    var id = $("#deletedId").val();
    $.ajax({
        url: '/iha/category/' + id + '/ ',
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

$(document).ready(function () {
    //md.initDashboardPageCharts();
   
    $('#editCategoryForm').submit(function (e) { // catch the form's submit event
        e.preventDefault();
        var formData = new FormData($(this)[0]);
        $.ajax({ // create an AJAX call...
            data: formData, // get the form data
            type: "PUT", 
            url: "/iha/category/" + $("#editId").val() + "/",
            processData: false,
            contentType: false,
            headers: {
                "X-CSRFToken": $crf_token,

            },
            success: function (response) {
                Swal.fire(
                    'Tebrikler!',
                    'Kategori Düzenlendi!',
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
            url: '/iha/category/' + ihaId + '/ ',
            type: 'GET',
            headers: {
                "X-CSRFToken": $crf_token
            },
            success: function (result) {
                $('#editModal').modal('show');
                $('[name="name"]').val(result.name);
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
            url: "iha/category/?format=datatables",
            type: "GET",
            error: function (data) {
                //can be used to log error
                console.log('Error:', data);
            },
        },
        "columns": [
        {
            data: "name",
            name: "name",
            searchable: true,
            width : "40%"
            },
            {
                data: "slug",
                name: "slug",
                searchable: true,
                width : "40%"
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
});