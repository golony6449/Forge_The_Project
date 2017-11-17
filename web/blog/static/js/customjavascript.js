/*
$("document").ready(function(){
  var nCard=1;
  var nContent=0;
  var i;

  $(window).resize(function() {
    var nCElement = $("#ContentsElement").length;

    if($(window).width()>=1570){
      nCard = 4;
    }else if($(window).width()>=1220){
      nCard = 3;
    }else if($(window).width()>=870){
      nCard = 2;
    }else{
      nCard = 1;
    }

    if((nCard - (nCElement%nCard))!= nContent){
      nContent = nCard-(nCElement%nCard);
      for(i=0;i<nContent;i++){
        $("#ContentsRow").append('<div class="col">'+$("#ContentsElement").html()+"</div>");
      }
    }
  })

  $(window).scroll(function() {

    if($(window).width()>=1570){
      nCard = 4;
    }else if($(window).width()>=1220){
      nCard = 3;
    }else if($(window).width()>=870){
      nCard = 2;
    }else{
      nCard = 1;
    }

    if ($(window).scrollTop() == $(document).height() - $(window).height())
    {
      //console.log(++page);
      //페이지 끝에 내용 추가
      //width>=1570 : 4cards, 1569>=width>=1220 : 3cards, 1219>=width>=870 : 2cards, width<=869 : 1card

      for(i=0;i<nCard;i++){
        $("#ContentsRow").append('<div class="col">'+$("#ContentsElement").html()+"</div>");
      }
    }
  });

});
*/
/*필터*/
function DisplayCard() {
  var x = document.getElementById("Filtercard");
  if(x.style.display==="none"){
    x.style.display = "block";
  }else{
    x.style.display="none"
  }
}
/*더보기 버튼*/
$(function(){
  $(".col").slice( 0, 8 ).show();
  $("#Viewmore").click(function(event){
    event.preventDefault();
    $(".col:hidden").slice( 0, 8 ).show();
    if($(".col:hidden").length == 0){
      $("#Viewmore").css("display","none");
    }
  })
});
