//waits until page is ready
$(document).ready(function () {

/*jQuery for the plus buttons on the FAQ page*/
    $(".answer").hide();

    // $(".plus-btn").click(function () {
    //     $(".answer").slideToggle(500);
    // });


    $(".plus-btn").on("click", function() {
      
        var thisAnswerSelector = "." + this.id + "answer";

        $(thisAnswerSelector).slideToggle(500);
        console.log('clicked');
    });
});