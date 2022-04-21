<template>
</template>
<script>
export default {
    data(){
        return {
            pageNumber: 0
        }
    },
    props:{
        listData:{
            type:Array,
            required:true
        },
        size:{
            type:Number,
            required:false,
            default: 20
        }
    },
    methods:{
        nextPage(){
            this.pageNumber++;
        },
        prevPage(){
            this.pageNumber--;
        }
    },
    computed:{
        pageCount(){
        let l = this.listData.length,
            s = this.size;
        return Math.floor(l/s);
        },
        paginatedData(){
        const start = this.pageNumber * this.size,
                end = start + this.size;
        return this.listData
                .slice(start, end);
        }
    }    
    }
</script>
<style>

</style>
