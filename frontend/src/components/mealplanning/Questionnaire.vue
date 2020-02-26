<template>
  <div>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
      <div class="demo-split">
        <Split v-model="split1">
          <div slot="left" class="demo-split-pane">
            <FormItem label="Name" prop="nameA">
              <Input v-model="formValidate.nameA" placeholder="Enter your name"></Input>
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
            <FormItem label="Taco" prop="foodA">
              <Slider v-model="formValidate.foodA[0]" show-input></Slider>
            </FormItem>
            <FormItem label="Rice" prop="foodA">
              <Slider v-model="formValidate.foodA[1]" show-input></Slider>
            </FormItem>
            <FormItem label="Noodle" prop="foodA">
              <Slider v-model="formValidate.foodA[2]" show-input></Slider>
            </FormItem>
            <FormItem label="Burger" prop="foodA">
              <Slider v-model="formValidate.foodA[3]" show-input></Slider>
            </FormItem>
            <FormItem label="Sushi" prop="foodA">
              <Slider v-model="formValidate.foodA[4]" show-input></Slider>
            </FormItem>
            <FormItem label="Budget" prop="budget">
              <Input v-model="formValidate.budget" placeholder="Enter your budget"></Input>
            </FormItem>
          </div>
          <div slot="right" class="demo-split-pane">
            <FormItem label="Name" prop="nameB">
              <Input v-model="formValidate.nameB" placeholder="Enter your name"></Input>
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
            <FormItem label="Taco" prop="foodB">
              <Slider v-model="formValidate.foodB[0]" show-input></Slider>
            </FormItem>
            <FormItem label="Rice" prop="foodB">
              <Slider v-model="formValidate.foodB[1]" show-input></Slider>
            </FormItem>
            <FormItem label="Noodle" prop="foodB">
              <Slider v-model="formValidate.foodB[2]" show-input></Slider>
            </FormItem>
            <FormItem label="Burger" prop="foodB">
              <Slider v-model="formValidate.foodB[3]" show-input></Slider>
            </FormItem>
            <FormItem label="Sushi" prop="foodB">
              <Slider v-model="formValidate.foodB[4]" show-input></Slider>
            </FormItem>
            <FormItem>
              <Button type="primary" @click="handleSubmit('formValidate')">Submit</Button>
              <Button @click="handleReset('formValidate')" style="margin-left: 8px">Reset</Button>
            </FormItem>
          </div>
        </Split>
      </div>
    </Form>
  </div>
</template>

<script>
export default {
  name: 'Questionnaire',
  data () {
    return {
      formValidate: {
        nameA: '',
        nameB: '',
        timeA: [0, 0, 0, 0, 0],
        timeB: [0, 0, 0, 0, 0],
        foodA: [0, 0, 0, 0, 0],
        foodB: [0, 0, 0, 0, 0],
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
      }
    }
  },
  methods: {
    handleSubmit (name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$Message.success('Success!')
        } else {
          this.$Message.error('Fail!')
        }
      })
    },
    handleReset (name) {
      this.$refs[name].resetFields()
    }
  }
}
</script>

<style scoped>
  .demo-split{
    margin: 0 100px;
    height: 60vh;
    border: 1px solid #dcdee2;
  }
  .demo-split-pane{
    padding: 50px;
  }
  .submit-button{
    text-align: center;
    margin-top: 20px;
  }
</style>
