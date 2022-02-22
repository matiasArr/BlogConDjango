var app = new Vue({
    el: '#app',
    data: {
      textInput: ''
    },
    methods: {
      getPost() {
        console.log("estamos dentro de getPost");
        //this.request(this.textInput);
      },
      request (q) {
        axios.get('search?q=' + q)
        .then(function (response) {
          // manejar respuesta exitosa
          data = response.data;
          //this.posts son objetos de post que fueron enviados desde el back
          this.posts = data.posts;
          //muestra la respuesta desde el front
          console.log(this.posts);
          this.response();
        })
        .catch(function (error) {
          // manejar error
          console.log(error);
        })
        .then(function () {
          // siempre sera executado
        });
      },
      response () {
        axios.post('', {
          firstName: 'Fred',
          lastName: 'Flintstone'
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    },
    
    //esto entrega un respuesta antes de que se realize una entrada de datos
    mounted () {
      this.getPost();
    }
    
  })