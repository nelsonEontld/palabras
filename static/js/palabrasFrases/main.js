alert('betom');


$.ajax({
	async: false,
	data: {'nombre': 'dog'},	
	url: '/pruebaFrases/busqueda_ajax/',
	type: 'get',
	success: function(result){
			console.log(result);
		}
});

