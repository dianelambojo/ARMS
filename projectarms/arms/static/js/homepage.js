//Book Slider
$(document).ready(function() {
  $('.slider').slick({
    centerMode: true,
    centerPadding: '100px',
    slidesToShow: 3,
    nextArrow: '<button type="button" class="btn btn-next"><i class="fa fa-arrow-right" aria-hidden="true"></i></button>',
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 3
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }
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
      var display = document.getElementById("searched");

      // Loop through the captions div 
      $(".thumbnail").each(function(){

          // If the div item does not contain the text phrase fade it out
          if ($(this).attr('title').search(new RegExp(filter, "i")) < 0) {
              $(this).fadeOut();
              $(".text").hide();
              $(".btn-next").hide();
          // Show the div item if the phrase matches 
          } else {
              $("#result").html("Results"+"<br>");
              $(this).show().appendTo("#searched");
              
              //$(".text").show();
              //$(".btn-next").show();
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

/*function openPDF(){
  var file = document.getElementById('pdfFile').val();
  window.open(file, "_blank");
}*/


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