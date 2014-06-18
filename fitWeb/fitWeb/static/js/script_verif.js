$(document).ready(inicio)

function inicio()
{
	$("#fregistro :input").blur(validar);
}

function validar(){
	
	if(this.id=='id_username'){
		var tusuario=this.value;
		$.ajax({
			type:'POST',
			url:'/verificar/usuario/',
			data:$('#fregistro').serialize(),
			beforeSend: antesEnviar,
			success: llegada,
			error:errores
			});
		//alert (tusuario);
	}
	//alert("hola");
}
function antesEnviar(){
	$("#resultado").text("Verificando...");
}
function llegada(data){
	$("#resultado").text(data);
}
function errores(){
	$("#resultado").text("Problemas en el servidor...");
}