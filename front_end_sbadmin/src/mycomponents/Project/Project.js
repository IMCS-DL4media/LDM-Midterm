import { mymixin } from '../mixins/mixins.js'

export default {
    mixins:[mymixin],
    props:['project_id'],
    data: function(){
        return {
            loading:false,	
            runs:[],
            runs1:[11,22,33],
            description:"",
            name:"",
            created_at:"",
            training_data_download_link:"",
            testing_data_download_link:"",
            error:null
        }
    },
    created () {
        //console.log(this.methods);
        //console.log(this);
        //console.log(this.SERVER_URL());
        // fetch the data when the view is created and the data is
        // already being observed
        this.fetchData()
    },
    watch: {
        // call again the method if the route changes
        '$route': 'fetchData'
    },		
    methods: {            
        getProjectDetails( project_id ) {	
            //console.log(process.env.VUE_APP_NODE_ENV);	
            console.log(project_id);
            var runs = fetch( this.SERVER_URL() +  'get_runs/'+project_id)
            .then(response=>response.json())
            .then(json => {
                this.runs = json.runs
                this.training_data_download_link = json.training_data_download_link
                this.training_file_size = json.training_file_size
                this.testing_data_download_link = json.testing_data_download_link
                this.testing_file_size = json.testing_file_size
                this.name = json.name
                this.description = json.description
                this.created_at = json.created_at
            })
            return (null,runs);
        },
        
        fetchData () {
            //console.log("fetch data")
            this.error = this.post = null
            this.loading = true
            // replace `getPost` with your data fetching util / API wrapper
            var res = this.getProjectDetails(this.project_id);
            
            this.loading = false
            if (res.err) {
                this.error = res.err.toString()
            } else {
                this.runs = res.runs
            }
        },

        get_first_10_symb( str ){
            if(str != null && str.length > 10){
                return str.substr(0,10);
            }
            return str;
        },

        uploadTestDataSetClicked:function(){
			let fileToUpload = this.$refs.fileInputRef.files[0];		
			let formData = new FormData();

            formData.append('project_id', this.project_id); 
			formData.append('zip_file', fileToUpload);
			
            
            console.log("//form data");
			console.log(formData);
			for (var key of formData.entries()) {
				console.log(key[0] + ', ' + key[1]);
            }
            console.log("//form data");

			this.$http.post(  this.SERVER_URL() + "upload_testing_data", formData)
				.then(response => {					
					console.log(response.body)				
                    //$('#alerts_success').show();
                    this.fetchData();
				},
				response => {						
					console.log(response.body)				
					//$('#alerts_fail').show();
				})
			
			return;
        },
        
        uploadTrainingDataSetClicked:function(){
			let fileToUpload = this.$refs.train_data_fileInputRef.files[0];
			let formData = new FormData();

            formData.append('project_id', this.project_id); 
			formData.append('zip_file', fileToUpload);
			
            
            console.log("//form data");
			console.log(formData);
			for (var key of formData.entries()) {
				console.log(key[0] + ', ' + key[1]);
            }
            console.log("//form data");

			this.$http.post(  this.SERVER_URL() + "upload_training_data", formData)
				.then(response => {					
					console.log(response.body)				
                    //$('#alerts_success').show();
                    this.fetchData();
				},
				response => {						
					console.log(response.body)				
					//$('#alerts_fail').show();
				})
			
			return;
        }
    }
}