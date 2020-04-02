import NavBar from './nav-bar'

describe('@components/nav-bar', () => {
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
