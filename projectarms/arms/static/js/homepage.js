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
    ],
  });
});

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
      var display = document.getElementById('display');

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


$(document).ready(function(){
  /*var mysql = require('mysql');

  var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "arms_database"
  });*/

  var style = $("#citeStyle :selected").val(); 

  if(style == "American Psychological Association"){
    document.getElementById('text').value = style;
  }

  $('#citeStyle').change(function() {
    var style = $("#citeStyle :selected").val(); 

    if(style == "American Psychological Association"){
      document.getElementById('text').value = style;

      /*con.connect(function(err) {
        if (err) throw err;
        
        con.query("SELECT * FROM books", function (err, result) {
          if (err) throw err;
          console.log(result);
        });
      });*/

    }else if(style == "Modern Language Association"){
      document.getElementById('text').value = style;
      console.log(style);
    }
  });

});



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

//TAGS//
[].forEach.call(document.getElementsByClassName('tags-input'), function (el) {
    let hiddenInput = document.createElement('input'),
        mainInput = document.createElement('input'),
        tags = [];
    
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', el.getAttribute('data-name'));

    mainInput.setAttribute('type', 'text');
    mainInput.classList.add('main-input');
 

    mainInput.addEventListener('keydown', function (e) {
        let keyCode = e.which || e.keyCode;
        if (keyCode === 8 && mainInput.value.length === 0 && tags.length >= 0) {
            removeTag(tags.length - 1);
        }

       if (keyCode === 13 && mainInput.value.length >= 0 && tags.length >= 0) {
             addTag(mainInput.value);
             mainInput.value ="";
        }


    });

    el.appendChild(mainInput);
    el.appendChild(hiddenInput);

    
     

    function addTag (text) {
        let tag = {
            text: text,
            element: document.createElement('span'),
        };

        tag.element.classList.add('tag');
        tag.element.textContent = tag.text;

        let closeBtn = document.createElement('span');
        closeBtn.classList.add('close');
        closeBtn.addEventListener('click', function () {
            removeTag(tags.indexOf(tag));
        });
        tag.element.appendChild(closeBtn);

        tags.push(tag);

        el.insertBefore(tag.element, mainInput);

        refreshTags();
        //run
    }

    function removeTag (index) {
        let tag = tags[index];
        tags.splice(index, 1);
        el.removeChild(tag.element);
        refreshTags();
    }

    function refreshTags () {
        let tagsList = [];
        tags.forEach(function (t) {
            tagsList.push(t.text);
        });
        hiddenInput.value = tagsList.join(',');
    }

    function filterTag (tag) {
        return tag.replace(/[^\w -]/g, '').trim().replace(/\W+/g, '-');
    }
});