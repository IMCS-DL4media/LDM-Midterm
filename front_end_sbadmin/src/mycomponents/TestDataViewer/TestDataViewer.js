import { mymixin } from '../mixins/mixins.js'
import { strict } from 'assert';

export default {
    
	name: "TestDataViewer",
	data: {
		showModal: false,
	},
	props: ['project_id'],
	components: {},
	mixins:[mymixin],
    
    data:function(){
		return {
            pageNumberInCurrChunk: 0,
            currChunkData : [],
            
            pageSize : 5,


            dataSetSize : 0,
            currChunkIndex : 0,
            chunkSize : 6,
            classes:[],
            isLoading:true,


            selectedClasses : new Map(),
            currClassName : "",
            training_data_labels:{},
            currIteratorPosition:{
                currClassIndex : 0,
                currFileStartIndex : 0
            },
            currChunkData1:[]


		}
    },
    
    
	created(){

        // this.dataSetSize = this.recieveDataSetSizeFromServer();
        // this.currChunkData = this.recieveDataFromServer(0, this.chunkSize);
        // var listOfClasses = this.recieveClassesFromServer()
        // if(listOfClasses != null){
        //     this.classes = new Map();
        //     for (let i = 0; i < listOfClasses.length; i++) {
                
        //         this.classes.set( listOfClasses[i], true );
        //     }
        //     console.log(this.classes)
        // }

        fetch( this.SERVER_URL() + 'get_training_data_labels/' + this.project_id )
            .then(function(response) {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response;
                })
            .then(response=>response.json())
            .then(json => {
                    console.log("in json ", json)
                    this.training_data_labels = json.data
                    console.log(this.training_data_labels)
                    
                    if( this.training_data_labels ){
                        for (let i = 0; i < Object.keys(this.training_data_labels).length; i++) {                
                            this.selectedClasses.set( Object.keys(this.training_data_labels)[i], true );
                        }
                        console.log(this.selectedClasses)
                    }
                    this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                    this.currChunkData1 = this.training_data_labels[this.currClassName].slice(this.currIteratorPosition.currFileStartIndex,this.currIteratorPosition.currFileStartIndex + 10)
                    this.isLoading = false
            }).catch(function(error) {
                console.log(error);
            });

	},

	methods:{
        // fakedata(){
        //     return [1,2,3,4,5,5,6];
        // },
        checkboxClicked(class_name, checkbox_id){
            var elem = document.getElementById(checkbox_id);
            //this checkbox just recieved a new value equal to elem.checked
            //console.log("checkbox clicked : " + elem.id + "  " + elem.checked )

            //gadijums kad uzstadam pirmo keksi pec situacijas, kad neviens keksis nebija uzstadits TODO
            let mapHasNoSelectedClasses = true

            for (let val of this.selectedClasses.values()) {
                if(val){
                    mapHasNoSelectedClasses = false
                }
            }
            //first click after all classes has been unselected 
            if(mapHasNoSelectedClasses && elem.checked){
                //currClassIndex index should correspond to class that has been selected
                //find index of class_name in this.training_data_labels
                let classInd = Object.keys(this.training_data_labels).indexOf(class_name) 
                if(  classInd == -1){
                    this.currIteratorPosition.currClassIndex = 0
                    this.currIteratorPosition.currFileStartIndex = 0
                    this.currChunkData1 = []
                    return
                }else{
                    this.currIteratorPosition.currClassIndex = classInd
                }

                this.currIteratorPosition.currFileStartIndex = 0
                console.log(this.currIteratorPosition.currClassIndex)
                this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                this.currChunkData1 = this.training_data_labels[this.currClassName].slice(this.currIteratorPosition.currFileStartIndex,
                                                                                          this.currIteratorPosition.currFileStartIndex + 10)

                console.log(class_name)
                if(this.selectedClasses.has(class_name)){
                    this.selectedClasses.delete(class_name)
                    console.log("after delete")
                    console.log( this.classes)
                }
                console.log( this.selectedClasses )
                this.selectedClasses.set( class_name , elem.checked );
                return
            }


            console.log(class_name)
            if(this.selectedClasses.has(class_name)){
                this.selectedClasses.delete(class_name)
                console.log("after delete")
                console.log( this.classes)
            }
            console.log( this.selectedClasses )
            this.selectedClasses.set( class_name , elem.checked );
            
            //what happens if we click on a currently selected class - unclick a class
            if(class_name == this.currClassName && elem.checked == false){//bija nonemts keksis no tas klases uz kuras dotaja bridi stavam
                if(this.canMoveBackward().isPossible ){
                    this.prevPage1()
                }else if(this.canMoveForward().isPossible){
                    this.nextPage1()
                }else{
                    this.currIteratorPosition.currClassIndex = 0
                    this.currIteratorPosition.currFileStartIndex = 0
                    console.log(this.currIteratorPosition.currClassIndex)
                    this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                    this.currChunkData1 = []
                    console.log(this.currChunkData1)
                }
            }


            
            console.log(this.selectedClasses);
        },

        canMoveForward(){
            let found = false
            let newClassInd = this.currIteratorPosition.currClassIndex
            let newFileStartInd = this.currIteratorPosition.currFileStartIndex
            
            while(!found){
                //check if we can move inside current class, if not try next class
                //this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                //console.log("d1",this.training_data_labels[this.currClassName])
                if( newFileStartInd + 10 <  this.training_data_labels[this.currClassName].length && this.selectedClasses.get(this.currClassName) ){
                    newFileStartInd += 10
                    found = true
                    break
                }


                if( newClassInd < Object.keys(this.training_data_labels).length ){
                    newClassInd++
                    const className_loc = Object.keys(this.training_data_labels)[newClassInd]
                    if( this.selectedClasses.get(className_loc) === true ){
                        found = true
                        newFileStartInd = 0
                        break
                    }
                }else{
                    found = false
                    break
                }
            }
            return {
                isPossible : found,
                newClassInd : newClassInd,
                newFileStartInd : newFileStartInd
            }
        },
        
        canMoveBackward(){
            let found = false
            let newClassInd = this.currIteratorPosition.currClassIndex
            let newFileStartInd = this.currIteratorPosition.currFileStartIndex
            
            while(!found){
                //check if we can move inside current class, if not try next class
                //this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                //console.log("d1",this.training_data_labels[this.currClassName])
                if( newFileStartInd - 10 >=  0 && this.selectedClasses.get(this.currClassName) ){
                    newFileStartInd -= 10
                    found = true
                    break
                }
                if( newClassInd > 0 ){
                    newClassInd--
                    const className_loc = Object.keys(this.training_data_labels)[newClassInd]
                    if( this.selectedClasses.get(className_loc) === true ){
                        found = true
                        //last ten files of this class
                        newFileStartInd = Math.max(0, this.training_data_labels[className_loc].length - 10) 
                        break
                    }
                }else{
                    found = false
                    break
                }
            }
            return {
                isPossible : found,
                newClassInd : newClassInd,
                newFileStartInd : newFileStartInd
            }
        },

        nextPage1(){
            //move next while selectedclasses[cl] = true and 
            console.log("next1")
            
            let res = this.canMoveForward()

            if( res.isPossible ){
                this.currIteratorPosition.currClassIndex = res.newClassInd
                this.currIteratorPosition.currFileStartIndex = res.newFileStartInd
                console.log(this.currIteratorPosition.currClassIndex)
                this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                this.currChunkData1 = this.training_data_labels[this.currClassName].slice(this.currIteratorPosition.currFileStartIndex, this.currIteratorPosition.currFileStartIndex + 10)
                console.log(this.currChunkData1)
            }

        },

        prevPage1(){
            console.log("prev1")
            let res = this.canMoveBackward()

            if( res.isPossible ){
                this.currIteratorPosition.currClassIndex = res.newClassInd
                this.currIteratorPosition.currFileStartIndex = res.newFileStartInd
                console.log(this.currIteratorPosition.currClassIndex)
                this.currClassName = Object.keys(this.training_data_labels)[this.currIteratorPosition.currClassIndex]
                this.currChunkData1 = this.training_data_labels[this.currClassName].slice(this.currIteratorPosition.currFileStartIndex, this.currIteratorPosition.currFileStartIndex + 10)
                console.log(this.currChunkData1)
            }
        },

        recieveDataSetSizeFromServer(){
            return 10;
        },

        recieveClassesFromServer(){
          return ["Bear", "Lion", "Camel"]
        },

        recieveDataFromServer(fromInd, toInd){
            this.isLoading = true
            console.log("recieveDataFromServer");
            console.log( "from ind = " + fromInd + " toInd = " + toInd)
            fetch( this.SERVER_URL() + 'get_training_data_set_chunk/' + this.project_id + "?fromInd=" + fromInd + "&toInd="+ toInd )
            .then(function(response) {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response;
                })
            .then(response=>response.json())
            .then(json => {
                    console.log("in json ", json)
                    this.currChunkData = json.data
                    this.isLoading = false
            }).catch(function(error) {
                console.log(error);
            });
            
            
            return this.createFakeData(fromInd, toInd);
        },

        recieveDataFromLocalServer(fromInd, toInd){
            console.log("recieveDataFromServer");
            console.log( "from ind = " + fromInd + " toInd = " + toInd)
            return this.createFakeData(fromInd, toInd);
        },

        createFakeData(fromInd, toInd){
            let data = [];
            for(let i = fromInd; i < toInd; i++){
              data.push({first: 'John',
                         last:'Doe', 
                         suffix:'#' + i});
            }
            return data;
        },

        recievePageData(){
          console.log("recievepagedata");
          const start = this.pageNumberInCurrChunk * this.pageSize,
                end = start + this.pageSize;
          //console.log(this.currChunkData);
          console.log("<>");
          console.log("recievePageData start = " + start + " end = " + end);
          console.log("res" + this.currChunkData);
          var res = this.currChunkData.slice(start, end);
          console.log("res " + res);
          console.log("</>");
          return res;
        },

        

        nextPage(){
           
           //japarbauda vai neesam izgajusi arpus tekosa chunka robezam
           if(this.pageNumberInCurrChunk * this.pageSize + this.pageSize >= this.chunkSize){
             //todo check if we can increment currchunkindex
                if( this.currChunkIndex * this.chunkSize + this.chunkSize >= this.dataSetSize){
                    //do nothing, we have no unvisited data
                    return;
                }else{
                    this.currChunkIndex++;
                }
                //this.currChunkData = this.recieveDataFromServer(this.currChunkIndex * this.chunkSize , this.currChunkIndex * this.chunkSize + this.chunkSize );
                this.currChunkData = this.recieveDataFromServer(this.currChunkIndex * this.chunkSize , Math.max(this.currChunkIndex * this.chunkSize + this.chunkSize, this.dataSetSize) );
                this.pageNumberInCurrChunk = 0;
           }else{
             this.pageNumberInCurrChunk++;
           }
        },

        prevPage(){            
            //japarbauda vai neesam izgajusi arpus tekosa chunka robezam
            if(this.pageNumberInCurrChunk * this.pageSize - this.pageSize < 0){
                //todo check if we can decrement currchunkindex
                if( this.currChunkIndex * this.chunkSize - this.chunkSize < 0){
                    //do nothing, we have no unvisited data
                    return;
                }else{
                    this.currChunkIndex--;
                }
                this.currChunkData = this.recieveDataFromServer(this.currChunkIndex * this.chunkSize , this.currChunkIndex * this.chunkSize + this.chunkSize );
                this.pageNumberInCurrChunk = 0;
                //must be last page in this chunk, not first
                while( this.pageNumberInCurrChunk * this.pageSize + this.pageSize < this.chunkSize ){
                    this.pageNumberInCurrChunk++;
                }
            }else{
                this.pageNumberInCurrChunk--;
            }
        }
    },
    computed:{
        pageCount(){
          let l = this.currChunkData.length,
              s = this.pageSize;
          return Math.ceil(l/s);
        }
        // paginatedData(){
        //   const start = this.pageNumberInCurrChunk * this.pageSize,
        //         end = start + this.pageSize;
        //   console.log(this.currChunkData);
        //   return this.currChunkData
        //            .slice(start, end);
        // }

   
      }
};
