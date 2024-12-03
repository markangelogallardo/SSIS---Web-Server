$(document).ready(function () {
    $("#collegeCode").select2();
    $('#collegeCode').on('select2:open', function() {
        var selectWidth = $(this).outerWidth();
        $('.select2-dropdown').css('width', selectWidth + 'px');
    });
});