var page = 2;

$(window).scroll(function() {
  if ($(window).scrollTop() == $(document).height() - $(window).height())
  {
    console.log(++page);
    //페이지 끝에 내용 추가
    //$("#mainbody").append('<div class="big-box"><h1>Page ' + page + '</h1></div>');
  }
});
$(document).ready(function(){
  $('.selectpicker').selectpicker({
  	container: 'body';
  });
  $('.dropdown-menu').on('click',function(event) {
  	event.stopPropagation();
  });
  $('#sel-menu').on('click',function(event) {
  	var target = $(event.target);
  	if (target.parents('.selectpicker').length) {
  		event.stopPropagation();
  		$('.selectpicker.open').removeClass('open');
  	}
  });
});
