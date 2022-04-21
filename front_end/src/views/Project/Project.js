import { mymixin } from '../../mixins/mixins.js'

export default {
    mixins:[mymixin],
    props:['project_id'],
    data: function(){
        return {
            loading:false,				
            runs:[],
            training_data_download_link:"",
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
        getPost( project_id ) {	
            //console.log(process.env.VUE_APP_NODE_ENV);	
            console.log(project_id);
            var runs = fetch( this.SERVER_URL() +  'get_runs/'+project_id)
            .then(response=>response.json())
            .then(json => {
                this.runs = json.runs
                this.training_data_download_link = json.training_data_download_link
            })
            return (null,runs);
        },
        
        fetchData () {
            this.error = this.post = null
            this.loading = true
            // replace `getPost` with your data fetching util / API wrapper
            var res = this.getPost(this.project_id);
            
            this.loading = false
            if (res.err) {
                this.error = err.toString()
            } else {
                this.runs = res.runs
            }
        }
    }
}