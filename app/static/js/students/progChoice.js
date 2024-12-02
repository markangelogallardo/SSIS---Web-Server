$(document).ready(function () {
    $("#prog_code").select2();
    $('#prog_code').on('select2:open', function() {
        var selectWidth = $(this).outerWidth();
        $('.select2-dropdown').css('width', selectWidth + 'px');
    });
});