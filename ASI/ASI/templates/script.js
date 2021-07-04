      var submit_form= function(){
        var id = document.getElementById("ins_id").innerHTML;
        console.log(id);
        try{
          fetch('', 
          {
            method : 'POST',
            body : "Anubhav Sharma"
          }
          )
        }
        catch(err){
          //console.log(${err});
        }
      };