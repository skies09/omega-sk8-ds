//waits until page is ready
$(document).ready(function () {

    /*jQuery for the plus buttons on the FAQ page*/
    $(".answer").hide();

    // $(".plus-btn").click(function () {
    //     $(".answer").slideToggle(500);
    // });

    $(".plus-btn").on("click", function() {
    var thisAnswer = "#" + this.id + "-answer";
    $(thisAnswer).slideToggle(500);


    // $(".plus-btn").on("click", function() {
    //     var thisAnswerSelector = "." + "question" +  this.id;
    //     $(thisAnswerSelector).slideToggle(500);
        console.log('clicked');
    });
  
});