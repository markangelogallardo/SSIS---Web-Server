$(document).ready(function () {
    // var cloudinaryImageSrc = $('#prof-pic').attr('src');
    // $('#upload-pic').val(cloudinaryImageSrc);
    $('#upload-pic').on('change', function(event) {
        event.preventDefault();
        const file = this.files[0];
        const reader = new FileReader();
        reader.onloadend = function() {
            $('#prof-pic').attr('src', reader.result);
            console.log(file)
        }
        if (file) {
            reader.readAsDataURL(file);
        } else {
            $('#imagePreview').attr('src', '');
        }
    
    });

    $('#reset-pic').on('click', function(event) {
        event.preventDefault();
        var default_pic = $("#default-profile").val()
       $('#upload-pic').val('');
        $('#prof-pic').attr('src', default_pic);
        //console.log($('#upload-pic').val())
    });
    $('#remove-pic').on('click', function(event) {
        event.preventDefault();
        const file = this.files[0];
        const reader = new FileReader();
        reader.onloadend = function() {
            $('#prof-pic').attr('src', reader.result);
        }
        if (file) {
            reader.readAsDataURL(file);
        } else {
            $('#prof-pic').attr('src', '');
        }
    });
});