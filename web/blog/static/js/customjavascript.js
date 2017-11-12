
$(window).scroll(function() {
  if ($(window).scrollTop() == $(document).height() - $(window).height())
  {
    //console.log(++page);
    //페이지 끝에 내용 추가
    $("#ContentsRow").append('');
  }
});

function DisplayCard() {
  var x = document.getElementById("Filtercard");
  if(x.style.display==="none"){
    x.style.display = "block";
  }else{
    x.style.display="none"
  }
}
