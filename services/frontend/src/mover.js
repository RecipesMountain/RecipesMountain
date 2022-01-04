import router from '@/router'

export const mover = {
    goToHome() {
        router.push("/")
    },
    goToSearch() {
        router.push("/search")
    },
    goToAccount() {
        router.push("/user")
    },
    goToLogin() {
        router.push("/login")
    },
    goToRegister() {
        router.push("/register")
    },
    goToAddRecipe() {
        router.push("/addRecipe")
    }

}