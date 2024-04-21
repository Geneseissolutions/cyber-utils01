from faker import Faker
import pyinputplus as pyip

fake_details_generator = Faker()


class FakeDetails:
    def __init__(self):
        self.fake_simple_profile = fake_details_generator.simple_profile()
        self.fake_profile = fake_details_generator.profile()

    def full_profile_generator(self):
        # use the Faker.profile() to generte a more detailed fake profile with more fake details
        print(
            f"""
              Fake Name: {self.fake_profile['name']}
              Fake Date of Birth : {self.fake_simple_profile['birthdate']}
              Gender : {self.fake_profile['sex']}
              Fake Email : {self.fake_profile['mail']}
              Fake Address : {self.fake_simple_profile['address']}
              Fake Job : {self.fake_profile['job']}
              Fake Company : {self.fake_profile['company']}
              Fake Blood Group : {self.fake_profile['blood_group']}
              Fake  Website : {self.fake_profile['website']}
              """
        )

    def less_details_profile_generator(self):
        # uses the Faker().simple_profile() to generate a profile with only basic details
        print(
            f"""Fake Name :{self.fake_simple_profile['name']}
                Fake Date of Birth: {self.fake_simple_profile['birthdate']}
                Gender : {self.fake_simple_profile['sex']}
                Fake Email:{self.fake_simple_profile['mail']}
                Fake Address:{self.fake_simple_profile['address']}
            """
        )


generator_object = FakeDetails()


def fake_profile_chooser():
    # validate user input by asking them to choose which profile to generate
    user_respose = pyip.inputMenu(
        ["Simple Fake Profile(few details)", "Complex Profile(more details)"],
        numbered=True,
        prompt="What type of profile would you like to generate : \n ",
    )

    if user_respose == "Simple Fake Profile(few details)":
        generator_object.less_details_profile_generator()
    if user_respose == "Complex Profile(more details)":
        generator_object.full_profile_generator()


if __name__ == "__main__":
    fake_profile_chooser()
