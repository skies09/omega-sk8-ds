function sendMail(contactForm) {
    emailjs.send("gmail", "omegaSkate", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "description": contactForm.description.value,
        })
.then(
        function(response) {
           alert("Your message has been sent");
            window.location ="{% url 'thanks' %}";
        },
        function(error) {
            console.log("FAILED", error);
            alert('Your message has not been sent');
            
        }
   );
           
}