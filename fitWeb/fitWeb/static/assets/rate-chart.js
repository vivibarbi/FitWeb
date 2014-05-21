	$(function() {
		$('.chart').easyPieChart({
			lineWidth:10,
			scaleColor: false,
			barColor: '#58c779',
			lineCap: 'butt',
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});
	});