import { mymixin } from '../mixins/mixins.js'

export default{	 
	props: ['run_id'],
	mixins: [mymixin],
	data: function() {
		return {
			loading:false,					
			run:{},
			error:null
		}
	},
	created () {
		// fetch the data when the view is created and the data is
		// already being observed
		//console.log('f data called')
		this.fetchData()
	},
	watch: {
		// call again the method if the route changes
		'$route': 'fetchData'
	},		
	methods: {

		getRunDetails( run_id ){
			console.log(run_id);
			fetch( this.SERVER_URL()  + 'get_run/'+run_id)
			.then(response=>response.json())
			.then(json => {
				this.run = json.run
			})
			return this.run;
		},
		
		fetchData () {
			this.error = this.post = null
			this.loading = true
			// replace `getPost` with your data fetching util / API wrapper
			var res = this.getRunDetails(this.run_id);
			
			this.loading = false
			this.run = res;
			
		}
	}		
};