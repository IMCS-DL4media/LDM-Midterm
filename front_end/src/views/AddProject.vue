<template>
   <div>
					<p>Start of component AddProject</p> <br> 
<!-- 
					<form :action="SERVER_URL()+'create_new_project'" method = "POST" 
						  enctype = "multipart/form-data">
						 Project name : 
						 <input type="text" name="project_name"/> <br>
						 Training file:
						 <input type = "file" name = "zip_file" /> <br>
						 
						 <input type = "submit" value="Create project"/>
					</form>
					
					<br/>
					<br/>
					 -->
					<form :action="SERVER_URL()+'create_new_project'" method = "POST" 
						  enctype = "multipart/form-data">
						
						<label>Project name: </label>
						<input type="text" name="project_name"/>
						
						<label>Training data: </label>
						<input type = "file" name = "zip_file" />
						
						<div>
							<input type = "submit" value="Create project" />
						</div>
					</form>
				

					<p>End of component</p> <br> 
		</div>
</template>

<script>
  import { mymixin } from '../mixins/mixins.js'
  export default{
    	mixins:[mymixin],
    	props:['project_id'],
		data: function(){
			return {
				loading:false,				
				runs:[],
				error:null
			}
		},
		created () {
      		//console.log(url());
			// fetch the data when the view is created and the data is
			// already being observed
			//this.fetchData()
		},
		watch: {
			// call again the method if the route changes
			//'$route': 'fetchData'
		},		
		methods: {
		
			getPost( project_id ){		
        		//this.url111();
				//console.log(project_id);
				//runs = fetch('http://127.0.0.1:5000/get_runs/'+project_id)
				//.then(response=>response.json())
				//.then(json => {
				//	this.res = json.res
				//})
				//return (null,runs);
			},
			
			fetchData () {
				this.error = this.post = null
				this.loading = true
				// replace `getPost` with your data fetching util / API wrapper
				res = this.getPost(this.project_id);
				
				this.loading = false
				if (res.err) {
				  this.error = err.toString()
				} else {
				  this.runs = runs
				}
			}
    }	
  }		
</script>

<style scoped>
form {
  /* Just to center the form on the page */
  margin: 0 auto;
  width: 400px;
  /* To see the outline of the form */
  padding: 1em;
  /* border: 1px solid #CCC; */
  /* border-radius: 1em; */
}

form div + div {
  margin-top: 1em;
}

label {
  /* To make sure that all labels have the same size and are properly aligned */
  display: inline-block;
  width: 90px;
  text-align: right;
}

input, textarea {
  /* To make sure that all text fields have the same font settings
     By default, textareas have a monospace font */
  /* font: 1em sans-serif; */

  /* To give the same size to all text fields */
  width: 300px;
  box-sizing: border-box;

  /* To harmonize the look & feel of text field border */
  border: 1px solid #999;
}

input:focus, textarea:focus {
  /* To give a little highlight on active elements */
  border-color: #000;
}

textarea {
  /* To properly align multiline text fields with their labels */
  vertical-align: top;

  /* To give enough room to type some text */
  /* height: 5em; */
}

.button {
  /* To position the buttons to the same position of the text fields */
  padding-left: 90px; /*same size as the label elements*/
}

button {
  /* This extra margin represent roughly the same space as the space
     between the labels and their text fields */
  margin-left: .5em;
}

</style>
