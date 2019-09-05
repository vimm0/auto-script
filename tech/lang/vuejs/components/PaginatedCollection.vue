<template>
    <div>
        <slot name="results" :results="results" :extraData="extra_data">
        </slot>
        <b-row v-if="isPaginated">
            <b-col>
                <p style="font-size: 0.8rem;color: #ccd0cc;">{{meta}}</p>
            </b-col>
            <b-col class="pagination-center">
                <b-pagination size="sm" :total-rows="count" :per-page="pageSize"
                              v-model="current"></b-pagination>
            </b-col>
        </b-row>
    </div>
</template>
<script>
    const PAGE_SIZE = 10;
    export default {
        props: ['endPoint', 'title', 'appName', 'resultPath', 'isPaginated', 'extraDataPath', 'refresh', 'extraData'],
        data() {
            return {
                currentEndPoint: this.endPoint,
                count: 0,
                meta: '',
                current: 1,
                pageSize: PAGE_SIZE,
                results: [],
                extra_data: null
            }
        },
        watch: {
            title: function () {
                this.$t(this.title)
            },
            current: function () {
                this.gotoPage(this.current)
            },
            endPoint: function (newVal, oldVal) {
                this.$_get(this.endPoint)
                this.current = 1
            },
            refresh: function () {
                this.gotoPage(this.current)
            },
            extra_data: function (newVal) {
                this.$emit('update:extraData', newVal)
            }
        },
        computed: {
            // pageTitle() {
            //     if (this.title && this.appName) {
            //         return `${this.$t(this.title)} - ${this.appName} | DSIS`
            //     } else if (this.title) {
            //         return `${this.$t(this.title)} | DSIS`
            //     } else {
            //         return 'DSIS'
            //     }
            // }
        },
        mounted() {
            // document.title = this.pageTitle
            // access message sent by siblings excelImporter
            this.$root.$on('updateAfterSuccess', data => {
                this.$_get(this.endPoint)
            });
        },
        methods: {
            $_get(url) {
                console.log(url)
                global.axios.get(url).then(
                    ({data}) => {
                        console.log(data)
                        if (this.extraDataPath) {
                            this.setExtraData(data)
                        }
                        if (this.resultPath) {
                            for (let i in this.resultPath) {
                                data = data[this.resultPath[i]]
                            }
                        }
                        this.currentEndPoint = url
                        this.count = data.count
                        // Vue.set(this.results, data.results)
                        this.$set(this.results, data.results)
                        // console.log(data)
                        this.results = data
                        this.meta = data.meta
                        this.$emit('paginatedData', data) // for option data rendering as message
                    }
                )
            },
            setExtraData(data) {
                if (this.extraDataPath) {
                    for (let i in this.extraDataPath) {
                        data = data[this.extraDataPath[i]]
                    }
                }
                this.extra_data = data
            },
            gotoPage(number) {
                let des = this.endPoint
                if (des.match(/\?/)) {
                    des = `${des}&page=${number}`
                } else {
                    if (!(des.endsWith('/'))) {
                        des = `${des}/`
                    }
                    des = `${des}?page=${number}`
                }
                this.$_get(des)
            }
        },
        created() {
            this.$_get(this.endPoint)
        }
    }
</script>
<style>
    .pagination-center {
        display: table;
        margin: 0 auto;
    }

    .page-item.active .page-link {
        color: #fff !important;
        z-index: 0 !important;
    }

    .page-item.active .page-link {
        color: #fff !important;
        background-color: #00bfd9 !important;
        border-color: #00bfd9 !important;
    }
</style>
