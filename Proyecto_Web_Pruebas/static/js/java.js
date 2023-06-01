

/*window.addEventListener("load", function() {
    setTimeout(function() {
        var imagen = document.getElementById("inicio");
        imagen.parentNode.removeChild(imagen);
        var menu = document.getElementById("menu");
        menu.style.display = "block";
    }, 2000);
});*/





/*$(document).ready(function() {
    setTimeout(function() {
        $(".content").fadeOut(1500);
},3000);
});*/





/*$(document).ready(function() {
    $(
   
'.content').fadeOut(5000, function() {
        $(
       
'#menu').fadeIn();
    });
});*/


    


   
/*$(document).ready(function() {
    // Agregar imagen a la página

    
    // Hacer que la imagen desaparezca gradualmente después de 5 segundos
    setTimeout(function() {
      $('#inicio').fadeOut(2000, function() {
        // Mostrar el menú después de que la imagen desaparezca
        $('#menu').fadeIn(1000);
      });
    }, 5000);
  });*/





  /*$(document).ready(function() {
    // Hacer que la imagen ocupe toda la pantalla
    $('#imagen').css({
      'position': 'fixed',
      'top': 0,
      'left': 0,
      'width': '100%',
      'height': '100%',
      'z-index': -1
    });
    
    // Hacer que el menú aparezca después de que la imagen desaparezca
    $('#imagen').on('click', function() {
      $(this).fadeOut(2000, function() {
        // Mostrar el menú después de que la imagen desaparezca
        $('#menu').fadeIn(1000);
      });
    });
  });*/

  $(document).ready(function() {
    setTimeout(function() {
        $(".content").fadeOut(1500);
    },3000);
 
    setTimeout(function() {
        $(".content2").fadeIn(1500);
    },5000);

    setTimeout(function() {
        $(".content3").fadeIn(1500);
    },5000);
    });
    
