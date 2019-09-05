import VueForm from '@/components/form/VueForm.vue'

export default {
  components: {VueForm},
  data() {
    let objId = null
    if (this.submitAsModal) {
      objId = this.formInstanceId
    } else {
      objId = this.$route.params.reference
    }
    return {
      fields: {},
      obj_id: objId
    }
  },
  watch: {
    formInstanceId: function (newVal) {
      this.initFetch()
    }
  },
  methods: {
    endpoint() {
      let endpoint = this.$options.endpoint
      // if (this.submitAsModal) {
      //   if (this.formInstanceId) {
      //     endpoint += this.formInstanceId + '/'
      //   }
      // } else if (this.$route.params.pk) {
      //   endpoint += this.$route.params.pk + '/'
      // }
      if (this.obj_id) {
        endpoint += this.obj_id + '/'
      }
      return endpoint
    },
    successCallback(data) {
      if (this.$options.success_url) {
        this.$router.push({path: this.$options.success_url})
      }
    },
    initFetch() {
      if (this.obj_id) {
        // console.log(this)
        global.axios.get(this.endpoint()).then(({data}) => {
          this.fields = data
        })
      }
      if (this.$options.dependencies) {
        this.$options.dependencies.forEach((model) => {
          global.axios.get(model.endpoint).then(({data}) => {
            this.$store.commit('update_collection', [model.collection_name, data])
          })
        })
      }
    }
  },
  computed: {
    success_message() {
      return this.$options.success_message || 'Saved'
    },
    pk() {
      // console.log(this)
      return this.$route.params.id
    }
  },
  created() {
    this.initFetch()
  },
  mounted() {
    // this.$on('success', this.successCallback)
  }
}
