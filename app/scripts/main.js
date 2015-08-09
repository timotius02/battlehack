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
			console.log('danger');
		}
		else if( date > lastWeek) {
			$(this).addClass('warning');
		}
	});

	var kitchenTabState = 'availableProduce';
	$('#available-produce-tab').on('click', function() {
		if (tabState !== 'availableProduce') {
			$('#order-history-tab').toggleClass('active');
			$(this).toggleClass('active');

			$('#order-history').toggle(false);
			$('#available-produce').toggle(true);
			tabState = 'availableProduce';
		}
	});
	$('#order-history-tab').on('click', function() {
		if (tabState !== 'orderHistory') {
			$('#available-produce-tab').toggleClass('active');
			$(this).toggleClass('active');

			$('#order-history').toggle(true);
			$('#available-produce').toggle(false);
			tabState = 'orderHistory';
		}
	});
});