//Jquery AJAX wird benutzt um die signup request an die Python Methode zu schicken
//Eine POST Methode für jquery wenn der Benutzer den Signup Knopf drückt
$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});