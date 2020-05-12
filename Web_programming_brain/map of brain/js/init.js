$(function(){
	var w = 1000;
	var h = 650;
	var r = Raphael("map", w, h),
	//здесь будет наш мозг

		attributes = {
            fill: "#E0E0E0",
			stroke: "#454545",
            'stroke-width': 2,
            'stroke-linejoin': 'round',
			"transform": "s0.8,0.8,0,0"     //Меняем размер,  например на s0.4,0.4,0,0
        }, //Это стиль оформления
		
	arr = new Array();
	
	for (var country in paths) {    //все отрисовываем
			var obj = r.path(paths[country].path);
			obj.attr(attributes);
		
			arr[obj.id] = country;
		
		obj
		.hover(function(){  //При наведении курсора мыши на определенный контур
			this.animate({
				fill: "#6E6E6E"
			}, 400);
		}, function(){
			this.animate({
				fill: attributes.fill
			}, 400);
		})
		
		.click(function(){
			//document.location.hash = arr[this.id];
			var point = this.getBBox(0);
			
			$('#map').next('.point').remove();  //удаляем существующий div 
			$('#map').after($('<div />').addClass('point')); //создаем новый
			
			$('.point')
			.html(paths[arr[this.id]].name)  //текст окна
			.prepend($('<a />').attr('href', '#').addClass('close').text('Close')) //кнопка закрытия
			
			.css({
				left: point.x+(point.width/2)-150,  //расположение выскакивающих окон
				top: point.y+(point.height/2)-50
			})
			.fadeIn();
			
		});
		
		$('.point').find('.close').live('click', function(){
			var t = $(this),
				parent = t.parent('.point');
			
			parent.fadeOut(function(){
				parent.remove();
			});
			return false;
		});
		
		
		 
		
	}
		
			
});



