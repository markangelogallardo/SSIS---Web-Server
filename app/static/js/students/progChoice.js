$(document).ready(function () {
    $("#prog_code").on("click", function(){
        console.log("you are inside")
    })
    $("#prog_code").select2({
        placeholder: 'Name',
        dropdownParent: $('#studForm')
    })
});