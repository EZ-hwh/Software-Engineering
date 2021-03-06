import NavBar from "./nav-bar-c";

describe('@components/nav-bar-c', () => {
  it(`displays the user's name in the profile link`, () => {
    const { vm } = shallowMount(
      NavBar,
      createComponentMocks({
        store: {
          auth: {
            state: {
              currentUser: {
                name: 'My Name',
              },
            },
            getters: {
              loggedIn: () => true,
            },
          },
        },
      })
    )
  })
})
