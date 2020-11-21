//Book Slider
$(document).ready(function() {
  $('.slider').slick({
    dots: true,
    infinite: false,
    speed: 700,
    slidesToShow: 4,
    slidesToScroll: 1,
    nextArrow: '<button type="button" class="btn btn-next"><i class="fa fa-arrow-right" aria-hidden="true"></i></button>',
    prevArrow: '<button type="button" class="btn btn-prev"><i class="fa fa-arrow-left" aria-hidden="true"></i></button>',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
});



/*function searchbyname(ele) {
  // Declare variabl
  const filter = jQuery(ele).val();

  $('.slider').slick('slickUnfilter');
  $('.slider').slick('slickFilter', function() {
    let content = jQuery(this).find("img").text().toLowerCase();
    return content.indexOf(filter) > -1;
  });
}*/


/*function allImages(){
    var imgs = document.getElementsByClassName("thumbnail");
    var search = document.getElementById("searchBox").value;
    var title = [];
    var display = document.getElementById("searched");
    var cl;

    for(var i = 0; i < imgs.length; i++) {
        title[i] = imgs[i].getAttribute('title');


        if(title[i] != null){
          if(title[i].toLowerCase() == search.toLowerCase()){
            //console.log(imgs[i].src);
            display.appendChild(imgs[i]);
            $(".text").hide();
            $(".btn-next").hide();
          }else{

          }
        }if(search == ""){
          display.remove();

          //console.log("null");
        }

    }
}*/

//Live Search -> not yet done
$(document).ready(function () {

  /*$(".thumbnail").hide();*/

  $("#searchBox").keyup(function(){

      // Retrieve the input field text 
      var filter = $(this).val();
      //var count = 0;
      var display = $("#display").val();

      // Loop through the captions div 
      $(".thumbnail").each(function(){

          // If the div item does not contain the text phrase fade it out
          if ($(this).attr('title').search(new RegExp(filter, "i")) < 0) {
              $(this).fadeOut();
              $(".text").hide();
              $(".btn-next").hide();
              $(".btn-prev").hide();
              $(".slick-dots").hide();

          
          } /*else if(filter.length == 0){
              $("#searched").val() = $(".slider").val();


          }*/
          // Show the div item if the phrase matches 
          else {
              $("#result").html("Results"+"<br>");
              $(this).show().appendTo("#display");
              $(".slider").hide();
              //$(this).show();
              //$(".text").show();
             // $(".btn-next").show();
              //$(".btn-prev").show();
              //$(".slick-dots").show();
              //count++;
          }
      });
      // Update the count
      /*var numberItems = count;
      $("#filter-count").text("Number of Filter = "+count);*/
   });
});





/*function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("searchBox");
  filter = input.value.toLowerCase();
  ul = document.getElementById("menu");
  li = ul.getElementsByTagName("li");

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("title")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toLowerCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}*/

function openPDF(){
  var file = document.getElementById('pdfFile').getAttribute('href');
  window.open(file, "_blank");
}


//Copy the auto generated citation to clipboard
function copyCitation() {
  /* Get the text field */
  var copyText = document.getElementById("citationText");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /*For mobile devices*/

  /* Copy the text inside the text field */
  document.execCommand("copy");
}

//Call the Toast for citation
$(document).ready(function(){
  $("#showToast").click(function(){
    $('.toast').toast('show');
  });
});


/*$(document).ready(function(){
  $('#citeStyle').change(function(){
    var style = $('#citeStyle :selected').text();
  });
});
*/


//Speech to Text feature
function runSpeechRecognition() {
    // new speech recognition object
    var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
    var search = document.getElementById("searchBox");


   
    // This runs when the speech recognition service starts
    recognition.onstart = function() {
        recognition.continous = true;
        //if('speechSynthesis' in window) {
          // Speech Synthesis supported 🎉
          //var msg = new SpeechSynthesisUtterance();
          //msg.text = "Good day! What can I do for you?";
         // window.speechSynthesis.speak(msg);
        //}else{
          // Speech Synthesis Not Supported 😣
        //  alert("Sorry, your browser doesn't support text to speech!");
        //}
        //console.log("We are listening. Try speaking into the microphone.");
    };

    recognition.onspeechend = function() {
        // when user is done speaking
        //recognition.stop();
        recognition.resume();
    }
                  
    // This runs when the speech recognition service returns result
    recognition.onresult = function(event) {
        var transcript = event.results[0][0].transcript;
        search.value = transcript;

        var filter = $("#searchBox").val();
        //var count = 0;
        var display = $('#display').val();

        // Loop through the captions div 
        $(".thumbnail").each(function(){

            // If the div item does not contain the text phrase fade it out
            if ($(this).attr('title').search(new RegExp(filter, "i")) < 0) {
                $(this).fadeOut();
                $(".text").hide();
                $(".btn-next").hide();
                $(".btn-prev").hide();
                $(".slick-dots").hide();

            // Show the div item if the phrase matches 
            } else {
                $("#result").html("Results"+"<br>");
                $(this).show().appendTo("#display");
                $(".slider").hide();

                //$(".text").show();
                //$(".btn-next").show();
                //count++;
            }
        });




        var confidence = event.results[0][0].confidence;
    };
                  
    // start recognition
    recognition.start();
}

