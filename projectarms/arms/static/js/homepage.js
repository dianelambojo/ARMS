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