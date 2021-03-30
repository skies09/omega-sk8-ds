//waits until page is ready
$(document).ready(function () {

    /*jQuery for the plus buttons on the FAQ page*/
    $(".answer").hide();

    $(".plus-btn").on("click", function () {
        var thisAnswer = "#" + this.id + "-answer";
        $(thisAnswer).slideToggle(500);

    });


});





