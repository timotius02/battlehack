$(window).ready(function() {
	var tabState = 'inventory';
	$('#inventory-tab').on('click', function() {
		if (tabState !== 'inventory') {
			$('#history-tab').toggleClass('active');
			$(this).toggleClass('active');

			$('#history').toggle(false);
			$('#inventory').toggle(true);
			tabState = 'inventory';
		}
	});

	$('#history-tab').on('click', function() {
		if (tabState !== 'history') {
			$('#inventory-tab').toggleClass('active');
			$(this).toggleClass('active');

			$('#history').toggle(true);
			$('#inventory').toggle(false);
			tabState = 'history';
		}
	});

	var today = new Date(Date.now());
	var lastWeek = new Date(today.getTime() - (60*60*24*7*1000));
	$('.expiration-date').map(function(index, element){
		var date = new Date($(this).text());
		if ( date > today) {
			$(this).addClass('danger');
		}
		else if( date > lastWeek) {
			$(this).addClass('warning');
		}
	});

	var kitchenTabState = 'availableProduce';
	$('#available-produce-tab').on('click', function() {
		if (kitchenTabState !== 'availableProduce') {
			$('#order-history-tab').toggleClass('active');
			$(this).toggleClass('active');

			$('#order-history').toggle(false);
			$('#available-produce').toggle(true);
			$('#select-grocery-store').toggle(false);
			kitchenTabState = 'availableProduce';
		}
	});
	$('#order-history-tab').on('click', function() {
		if (kitchenTabState !== 'orderHistory') {
			$('#available-produce-tab').toggleClass('active');
			$(this).toggleClass('active');

			$('#order-history').toggle(true);
			$('#available-produce').toggle(false);
			$('#select-grocery-store').toggle(false);
			kitchenTabState = 'orderHistory';
		}
	});

	$('.select-produce').on('click', function() {
		if(kitchenTabState !== 'selectGroceryStore') {
			$('#order-history').toggle(false);
			$('#available-produce').toggle(false);
			$('#select-grocery-store').toggle(true);

			kitchenTabState = 'selectGroceryStore';
		}
	});

	$('.back-to-map').on('click', function() {
		if(kitchenTabState === 'selectGroceryStore') {
			$('#select-grocery-store').toggle(false);
			$('#available-produce').toggle(true);
			
			kitchenTabState = 'availableProduce';
		}
	});


		$("#sell").on("click", function (e) {
				e.preventDefault();
				var price= $("#sellingPrice").val();
				var selected= $("input[type='radio'][name='tableoption']:checked").val();
				var data = {price: price, id: selected, sale: true};
				$.ajax({
						type:"POST",
						url:"/listProduct",
						data: JSON.stringify(data, null, '\t'),
						contentType: 'application/json;charset=UTF-8',
						success: function(result) {
								console.log(result);
						}
				});
		});


		$("#donate").on("click", function (e) {
			e.preventDefault();
			var price= $("#sellingPrice").val();
			var selected= $("input[type='radio'][name='tableoption']:checked").val();
			var data = {price: 0, id: selected, sale: true};
			$.ajax({
					type:"POST",
					url:"/listProduct",
					data: JSON.stringify(data, null, '\t'),
					contentType: 'application/json;charset=UTF-8',
					success: function(result) {
						console.log(result);
					}
			});
		});


		$("#purchase").on("click", function (e) {
				e.preventDefault();
				var selected= $("input[type='checkbox'][name='purchaseCheck']:checked").val();
				console.log(selected)
				var data = {price: selected};
//				$.ajax({
//						type:"POST",
//						url:"/foopayments",
//						data: JSON.stringify(data, null, '\t'),
//						contentType: 'application/json;charset=UTF-8',
//						success: function(result) {
//								console.log(result);
				window.location=window.location.origin +'/payments?amount=' + selected;
//						}
//				});
		});

		



});



