$(document).ready(function(){
	var path_to_compare = '';
	$("a[name='compare']").click(function(e){
		path_to_compare += $(e.target).attr('id') + '/';
		console.log(path_to_compare);
	});
});