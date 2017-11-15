function LoadingContents() {
  $(window).scroll(function() {
    var nCard =1;
    var i;
    var code = '<div class="col"><div class="card" style="width: 20rem;"><img class="card-img-top" src="Demo/Icon/resized-DefaultImage.png" alt="Card image cap"><div class="card-block"><h4 class="card-title">Project title</h4><p class="card-text">Describe Your Project</p><a href="#" class="btn btn-secondary">Go Pjt-Room</a></div></div></div>';
    if ($(window).scrollTop() == $(document).height() - $(window).height())
   {
      if($(window).width()>=1570){
        nCard=4;
    }else if($(window).width()>=1220){
        nCard=3;
    }else if($(window).width()>=870){
       nCard=2;
    }else{
        nCard=1;
     }
      for(i=0;i<nCard;i++){
      $("#ContentsRow").append(code);
      }
   }
  });
}


function DisplayCard() {
  var x = document.getElementById("Filtercard");
  if(x.style.display==="none"){
    x.style.display = "block";
  }else{
    x.style.display="none"
  }
}
