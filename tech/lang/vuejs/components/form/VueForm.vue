<template>
  <form method="POST" enctype="multipart/form-data" @submit.prevent="save(action)" @focusin="errors.clear($event)">
    <slot name="form-header">
    </slot>

    <slot name="form-fields" :errors="errors">
    </slot>

    <div class="text-xs-right">
      <slot name="submit" :remove="remove" :fields="fields" :errors="errors" :save="save" :action="action">
        <button class="btn btn-primary notika-btn-primary waves-effect mr-1 mt-2 mb-2"
                @click.prevent="save(action)"
                v-if="fields.reference || fields.id"
                :disabled="errors.any()"><i class="notika-icon notika-checked"></i> Update
        </button>

        <button class="btn btn-primary notika-btn-primary waves-effect mt-2 mb-2" @click.prevent="save(action)"
                :disabled="errors.any()"
                v-else><i class="notika-icon notika-checked"></i> Create
        </button>
        <button class="btn btn-danger notika-btn-danger waves-effect mt-2 mb-2" @click.prevent="remove(action)"
                v-if="fields.reference || fields.id"><i
          class="fa fa-trash-o"></i>
          Delete
        </button>

        <slot name="extra_actions">
        </slot>
      </slot>
    </div>
  </form>
</template>
<script>
  class Errors {
    constructor() {
      this.errors = {}
    }

    has(field) {
      return this.errors.hasOwnProperty(field)
    }

    any() {
      return Object.keys(this.errors).length > 0
    }

    get(field) {
      if (this.errors[field]) {
        return this.errors[field][0]
      }
    }

    nestedGet(...args) {
      let value = null
      for (let arg in args) {
//        console.log(args[arg])
        if (this.errors[args[arg]]) {
          value = this.errors[args[arg]]
        }
      }
      return value
    }

    record(errors) {
      this.errors = errors
    }

    clear(event = null) {
      if (event) {
        const field = event.target.name
        if (event.target.getAttribute('row') === 'true' && this.errors.hasOwnProperty('rows')) {
          global.Vue.delete(this.errors, 'rows')
          return
        }
        if (field) {
          global.Vue.delete(this.errors, field)
          return
        }
      }
      this.errors = {}
    }
  }

  export default {
    props: ['fields', 'action', 'title', 'appName', 'submitAsModal', 'defaultFieldsValues', 'successUrl', 'enableResetFormOnSuccess', 'formInstanceId'],
    data() {
      let dct = {}
      dct.original_fields = Object.assign({}, this.fields)
      dct.field_names = []
      for (let field in this.data) {
        dct.field_names.push(field)
      }
      dct.errors = new Errors()
      return dct
    },
//    created(){
//    },
//         computed: {
//             pageTitle() {
//                 if (this.title) {
//                     return `${this.title} - ${this.appName} | DSIS`
//                 } else {
//                     return 'DSIS'
//                 }
//             }
//         },
//         mounted() {
//             document.title = this.pageTitle
//         },
    methods: {
      reset() {
        this.errors.clear()
      },
      getFieldsData() {
        let payload = this.fields
        if (this.defaultFieldsValues !== 'undefined') {
          payload = Object.assign({}, payload, this.defaultFieldsValues)
        }

        return payload
      },
      save(url) {
        let verb
        // console.log(this)
        if (this.fields.reference || this.formInstanceId || this.fields.id) {
          verb = 'put'
        } else {
          verb = 'post'
        }
        this.submit(verb, url)
      },
      post(url) {
        return this.submit('post', url)
      },
      put(url) {
        return this.submit('put', url)
      },
      patch(url) {
        return this.submit('patch', url)
      },
      remove(url) {
        return this.submit('delete', url)
      },
      resetForm() {
        Object.assign(this.fields, this.original_fields)
      },
      submit(requestType, url) {
        // console.log(requestType)
        // console.log(this.getFieldsData())
        var bool = true;
        if (requestType === 'delete') {
          var r = confirm("Are you sure you want to delete?");
          if (r === true) {
            bool = true
          } else {
            bool = false
          }
        }
        // console.log(bool)
        if (bool === true) {
          // console.log(this.getFieldsData())
          return new Promise((resolve, reject) => {
            global.axios[requestType](url, this.getFieldsData())
              .then(({data}) => {
                this.onSuccess(data)
                if (requestType === 'put') {
                  console.log(`The ${this.$route.name.split(' ')[0]} "${data.text}" was changed successfully.`)
                  this.$toasted.show(`The ${this.$route.name.split(' ')[0]} "${data.text}" was changed successfully.`, {
                    type: 'success',
                    duration: 3200
                  })

                } else if (requestType === 'post') {
                  this.$toasted.show(`The ${this.$route.name.split(' ')[0]} "${data.text}" was created successfully.`, {
                    type: 'success',
                    duration: 3200
                  })
                  // this.$toasted.global.toast_create();
                } else if (requestType === 'delete') {
                  this.$toasted.show(`The ${this.$route.name.split(' ')[0]} "${data.text}" was deleted successfully.`, {
                    type: 'info',
                    duration: 3200
                  })
                  // this.$toasted.global.toast_delete();
                }
                if (this.submitAsModal) {
                  this.$emit('saveAsModal', data) // catch by Modal.vue, to update selectize options
                } else {
                  if (this.successUrl) {
                    this.$emit('success', data, this.successUrl)
                  } else {
                    this.$emit('success', data)
                  }
                }
                if (this.enableResetFormOnSuccess) {
                  this.resetForm()
                }
                resolve(data)
              })
              .catch(error => {
                // console.log(requestType)
                if (requestType === 'delete') {
                  this.onFail(error.response.data)
                  this.$toasted.global.toast_delete();
                }
                this.onFail(error.response.data)
                // this.$parent.$emit('failure', error.response.data)
                reject(error.response.data)
              })

          })
        }
      },
      onSuccess(data) {
        this.reset()
      },
      onFail(errors) {
        console.log(errors.hasOwnProperty('error'))
        console.log(errors)
        if (errors.hasOwnProperty('error')) {
          this.$error(errors.error[0])
          setTimeout(() => {
            global.Vue.delete(this.errors.errors, 'error')
          }, 1000)
        }
        this.errors.record(errors)
      }
    }
  }
</script>
