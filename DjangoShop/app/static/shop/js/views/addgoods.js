$(function(){
    'use strict';
    $("body").delegate('#goodimg', 'change', function () {
        $("#goodPreview").attr("src", window.URL.createObjectURL(this.files[0]));
    });
    $("#backtolist").click(function () {
        location.href = "/goodlist?" + getCookie("parentpage");
    });
});
