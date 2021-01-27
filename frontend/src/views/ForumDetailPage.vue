<template>
  <div class="row" style="margin:0 auto; width: 1200px; height: 600px;">
    <div class="justify-center col-9">
      <div class="q-pa-md row items-start q-gutter-md">
        <q-card flat bordered class="my-card" style="padding: 30px;">
          <q-card-section>
            <div class="text-h4">
              <b>{{ title }}</b>
            </div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <div class="row">
              <div class="col-0.5">
                <span style="cursor:pointer; margin-right: 11px;">
                  <q-avatar
                    @click="goToProfile"
                    style="width: 35px; height: 35px;"
                    ><img :src="profile_img" />
                  </q-avatar>
                </span>
              </div>
              <div class="col-11.5">
                <div
                  style="font-size: 15px; cursor:pointer; height: 17px; color: #464646"
                  @click="goToProfile"
                >
                  <b>{{ username }}</b>
                </div>
                <span style="font-size: 10px; color: #464646">15분 전</span>
              </div>
            </div>
          </q-card-section>
          <br />
          <q-card-section class="q-pt-none">
            <div v-for="i in 3" :key="i">
              <span class="icon-position" style="margin-left: 10px;">
                <q-badge color="blue">
                  # Vue
                </q-badge>
              </span>
            </div>
          </q-card-section>
          <br />
          <br />
          <q-card-section class="q-pt-none">
            <p style="font-size:40px;">Hello world!</p>
            <p style="font-size:20px;">testing</p>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio
              omnis sunt a nisi? Ratione nisi sunt sequi neque sapiente expedita
              placeat repellat eos dolorem voluptas. Alias officia fugit rem et
              eveniet. Architecto dicta aliquam optio odit autem tenetur?
              Reprehenderit, dolorum? Quibusdam quam odio neque ullam enim totam
              voluptatum est culpa quas, similique velit esse quos tenetur
              molestiae voluptatem perferendis minima assumenda ex! Rem
              explicabo sunt, beatae pariatur animi minima dolores iste eius
              tenetur officia praesentium architecto quos facere, ab doloremque?
              Soluta mollitia asperiores nostrum dolorem debitis! Nihil enim
              vero, ad obcaecati error ab nesciunt neque. Voluptatibus, ullam
              praesentium sapiente possimus non enim suscipit mollitia vitae
              deleniti, nesciunt esse magnam natus, minima quam. Omnis ut,
              ratione nulla modi aliquam nesciunt laboriosam repellat a hic
              quasi ab magnam sed, minima voluptate neque dignissimos fuga iure!
              Dolore, magni ad enim dolorum nostrum exercitationem. Omnis
              accusantium modi accusamus. Velit doloremque nam autem et
              accusantium labore odit veritatis. Dicta consequuntur, vel harum
              rem soluta nemo at beatae blanditiis corporis quaerat. Neque
              nulla, rerum odit fugiat perferendis voluptatum ipsa quibusdam id
              pariatur dolores a tempore repellat dolor iure aut explicabo ut
              reprehenderit doloribus cum ipsam nemo, excepturi, assumenda quam
              vitae. Quod hic quia saepe. Ipsum, quidem?<br />
              <br />
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui
              deserunt cum voluptates eaque magnam fugiat at, excepturi
              distinctio rerum accusantium ut in deleniti iste, expedita ducimus
              ipsum libero autem! Maiores nam odio, nemo numquam distinctio
              animi perferendis quis iste ab! Suscipit ab, ipsam minima nostrum
              quo eveniet distinctio architecto hic. Eaque quam, obcaecati
              soluta eligendi deleniti exercitationem natus et impedit
              recusandae? Atque consequuntur, nulla eveniet itaque suscipit
              temporibus necessitatibus blanditiis exercitationem quod,
              perspiciatis ad praesentium odit sunt voluptas impedit neque
              facilis! Corrupti iure neque, quae ducimus rerum ab doloremque
              labore quod ipsam? Obcaecati eligendi explicabo odio molestiae
              necessitatibus aliquam cum.
            </p>
          </q-card-section>
        </q-card>
        <ForumComment></ForumComment>
      </div>
    </div>

    <div class="col-3">
      <ForumShortProfile></ForumShortProfile>
    </div>
  </div>
</template>

<script>
import ForumShortProfile from '@/components/forum/ForumShortProfile';
import ForumComment from '@/components/forum/ForumComment';

export default {
  components: {
    ForumShortProfile,
    ForumComment,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
