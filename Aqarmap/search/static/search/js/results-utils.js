$(document).ready(function(){
	var path_to_compare = '';
	var click_count = 0;
	$("a[name='compare']").click(function(e){
		path_to_compare += $(e.target).attr('id') + '/';
		click_count++;
		$(e.target).addClass('btn-info')
		if (click_count == 2) {
			var site_url = "http://127.0.0.1:8000/search/compare/";
			$(location).attr('href',site_url+path_to_compare)
		}
	});
});