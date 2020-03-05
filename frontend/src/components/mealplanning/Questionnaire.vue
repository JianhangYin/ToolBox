<template>
  <div>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="100" label-position="left">
      <div class="demo-split">
        <Split v-model="split">
          <div slot="left" class="demo-split-pane">
            <FormItem label="Name" prop="nameA">
              <Input v-model="formValidate.nameA" placeholder="Enter your name"/>
            </FormItem>
            <FormItem label="Free Time" prop="timeA">
              <CheckboxGroup v-model="formValidate.timeA">
                <Checkbox label="Monday"></Checkbox>
                <Checkbox label="Tuesday"></Checkbox>
                <Checkbox label="Wednesday"></Checkbox>
                <Checkbox label="Thursday"></Checkbox>
                <Checkbox label="Friday"></Checkbox>
              </CheckboxGroup>
            </FormItem>
            <FormItem :label="foodList[0]" prop="foodA" :label-width="400">
              <Rate v-model="formValidate.foodA[0]" />
            </FormItem>
            <FormItem :label="foodList[1]" prop="foodA" :label-width="400">
              <Rate v-model="formValidate.foodA[1]" />
            </FormItem>
            <FormItem :label="foodList[2]" prop="foodA" :label-width="400">
              <Rate v-model="formValidate.foodA[2]" />
            </FormItem>
            <FormItem :label="foodList[3]" prop="foodA" :label-width="400">
              <Rate v-model="formValidate.foodA[3]" />
            </FormItem>
            <FormItem :label="foodList[4]" prop="foodA" :label-width="400">
              <Rate v-model="formValidate.foodA[4]" />
            </FormItem>
            <FormItem label="Budget" prop="budget">
              <Input v-model="formValidate.budget" placeholder="Enter your budget"/>
            </FormItem>
          </div>
          <div slot="right" class="demo-split-pane">
            <FormItem label="Name" prop="nameB">
              <Input v-model="formValidate.nameB" placeholder="Enter your name"/>
            </FormItem>
            <FormItem label="Free Time" prop="timeB">
              <CheckboxGroup v-model="formValidate.timeB">
                <Checkbox label="Monday"></Checkbox>
                <Checkbox label="Tuesday"></Checkbox>
                <Checkbox label="Wednesday"></Checkbox>
                <Checkbox label="Thursday"></Checkbox>
                <Checkbox label="Friday"></Checkbox>
              </CheckboxGroup>
            </FormItem>
            <FormItem :label="foodList[0]" prop="foodB" :label-width="400">
              <Rate v-model="formValidate.foodB[0]" />
            </FormItem>
            <FormItem :label="foodList[1]" prop="foodB" :label-width="400">
              <Rate v-model="formValidate.foodB[1]" />
            </FormItem>
            <FormItem :label="foodList[2]" prop="foodB" :label-width="400">
              <Rate v-model="formValidate.foodB[2]" />
            </FormItem>
            <FormItem :label="foodList[3]" prop="foodB" :label-width="400">
              <Rate v-model="formValidate.foodB[3]" />
            </FormItem>
            <FormItem :label="foodList[4]" prop="foodB" :label-width="400">
              <Rate v-model="formValidate.foodB[4]" />
            </FormItem>
            <FormItem>
              <Button type="primary" @click="handleSubmit('formValidate')">Submit</Button>
              <Button @click="handleReset('formValidate')" style="margin-left: 8px">Reset</Button>
            </FormItem>
            <FormItem>
              <Button type="error" @click="modal = true">Web Scraping</Button>
            </FormItem>
          </div>
        </Split>
      </div>
    </Form>
    <Modal v-model="modal" width="400">
      <p slot="header" style="color:#f60;text-align:center">
        <Icon type="ios-information-circle"></Icon>
        <span>Attention</span>
      </p>
      <div style="text-align:center">
        <p>Are you sure to update the recipe database?</p>
        <p>It will take about 3 minutes.</p>
      </div>
      <div slot="footer">
        <Button type="error" size="large" long :loading="modal_loading" @click="webScraping">Confirm</Button>
      </div>
    </Modal>
  </div>
</template>

<script>
export default {
  name: 'Questionnaire',
  data: function () {
    return {
      formValidate: {
        nameA: '',
        nameB: '',
        timeA: [],
        timeB: [],
        foodA: [0.0, 0.0, 0.0, 0.0, 0.0],
        foodB: [0.0, 0.0, 0.0, 0.0, 0.0],
        budget: 0
      },
      ruleValidate: {
        nameA: [
          { required: true, message: 'The name cannot be empty', trigger: 'blur' }
        ],
        nameB: [
          { required: true, message: 'The name cannot be empty', trigger: 'blur' }
        ],
        budget: [
          { required: true, message: 'Budget cannot be zero', trigger: 'blur' },
          { type: 'number',
            message: 'Incorrect budget format',
            trigger: 'blur',
            transform (value) { return Number(value) }
          }
        ]
      },
      split: 0.5,
      modal_loading: false,
      modal: false,
      foodList: ['loading...', 'loading...', 'loading...', 'loading...', 'loading...']
    }
  },
  created: function () {
    this.$axios.get(
      '/api/get-five-recipe'
    )
      .then(response => {
        this.foodList = response.data.recipe.map(item => item[0])
      })
      .catch(error => {
        console.log(error, 'error')
      })
  },
  methods: {
    handleSubmit (name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$axios.post(
            '/api/meal-planning',
            {
              nameA: this.formValidate.nameA,
              nameB: this.formValidate.nameB,
              timeA: this.formValidate.timeA,
              timeB: this.formValidate.timeB,
              foodA: this.formValidate.foodA,
              foodB: this.formValidate.foodB,
              budget: this.formValidate.budget,
              foodList: this.foodList
            }
          )
            .then(response => {
              console.log(response, 'success')
              this.$router.push({
                name: 'MealPlan',
                params: {
                  data: response.data
                }
              })
              this.toast(true, 'Submit success!')
            })
            .catch(error => {
              console.log(error, 'error')
              this.toast(false, 'Submit fail!')
            })
        } else {
          this.$Message.error('Form validation fail!')
        }
      })
    },
    handleReset (name) {
      this.$refs[name].resetFields()
    },
    webScraping () {
      this.modal_loading = true
      this.$axios.get(
        '/api/web-scraping'
      )
        .then(response => {
          this.modal_loading = false
          this.modal = false
          console.log(response, 'success')
          this.toast(true, 'Database updated!')
        })
        .catch(error => {
          this.modal_loading = false
          this.modal = false
          console.log(error, 'error')
          this.toast(false, 'Web scraping fail!')
        })
    },
    toast (ifSuccess, word) {
      if (ifSuccess) {
        this.$Message.success(word)
      } else {
        this.$Message.error(word)
      }
    }
  }
}
</script>

<style scoped>
  .demo-split{
    margin: 0 100px;
    height: 65vh;
    border: 1px solid #dcdee2;
  }
  .demo-split-pane{
    padding: 50px;
  }
</style>
