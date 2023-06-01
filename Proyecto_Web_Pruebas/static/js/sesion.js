const usuariosPermitidos = {
    "pruebas": "12345",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
  };
  
  function login() {
    const user = document.getElementById("usuario").value;
    const password = document.getElementById("contrasena").value;
  
    if (usuariosPermitidos[user] === password) {
      window.location = "/prueba";
    
     
    } else {
      alert("Usuario o contraseña incorrectos");
    }
  }
    