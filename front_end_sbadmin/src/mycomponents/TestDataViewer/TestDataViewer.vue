<template>
    <div>
<div class ="container">
        <!-- ProjectID : {{project_id}} -->
        <div v-if="!isLoading" class="row">
            <div class = "col-sm-3 ">
				<!--
					Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
				-->
                    <br/>
                    <!-- List of checboxes -->
					Gold labels:
					<br/>
					<br/>
                    <!-- <input type="checkbox" disabled> ClassName 1<br/>
                    <input type="checkbox" disabled> ClassName 2<br/>
                    <input type="checkbox" disabled> ClassName 3<br/>
                    <input type="checkbox" disabled> ClassName 4<br/>
					<br/> -->
					

                    <div v-for="cl in Object.keys(this.training_data_labels)" :key="cl">
                        <span :class="{'font-weight-bolder h5':currClassName == cl}">
                            <input type="checkbox" :id="'id' + cl" checked @click = "checkboxClicked( cl, 'id' + cl )"> 
                                {{cl}}   
                                ({{training_data_labels[cl].length}}) <br/>
                        </span>
                    </div>
                    <br/>
					<!-- Silver labels:
					<br/>
					<br/> -->
                    <!-- <div v-for="cl in this.classes.keys()" :key="cl">
                        <input type="checkbox" :id="'id' + cl" checked @click = "checkboxClicked( cl, 'id' + cl )" > {{cl}} <br/>
                    </div> -->
                    <br/>
            </div>
    
            <div class = "col-sm-9">
                <!--
					Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
				-->
                <!-- <br/> -->
                
                
                <div class = "row" >
                    <div class = "col" v-for="p in this.currChunkData1">
                        <img height = "150" width = "150" :src=" SERVER_URL() + 'get_training_file/' + p + `?project_id=` + project_id "  >
                        <div>Gold label : {{currClassName}}</div>
                        <!-- <div>Silver label : Sunflower</div> -->
                        <div>File name : {{p}}</div>
                    </div>
                </div>
<!-- 
                <div class = "row" >
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
                        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>
                    </div>
                
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
                        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>
                    </div>
                
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>                
                    </div>
                    
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
                        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>
                    </div>
                
					<div class="col">
						<img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
						alt="Smiley face" height="150" width="150">
						
						<div>Gold label : Sunflower</div>
						<div>Silver label : Sunflower</div>
					</div>

					
                
                </div> -->
                
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                
				
				
					<!-- <nav aria-label="Page navigation example" >
                        <ul class="pagination justify-content-center">
                            <li class="page-item"><a class="page-link" href="#" >Previous</a></li>
                            <li class="page-item"><a class="page-link" href="#">1</a></li>
                            <li class="page-item"><a class="page-link" href="#">2</a></li>
                            <li class="page-item"><a class="page-link" href="#">3</a></li>
                            <li class="page-item"><a class="page-link" href="#">Next</a></li>
                        </ul>
					</nav> -->

                <br/>
                
                <div class ="row justify-content-center">
                    <button @click="prevPage1">Previous </button>
                    <button @click="nextPage1">Next</button>
                </div>
				
            </div>
			

        </div>
    </div>






        
    </div>




</template>

<script src="./TestDataViewer.js"></script>