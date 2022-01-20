export const getInitials = (fullName) => {
    if(fullName == null) return "PW" 
    const words = fullName.split(" ")
    return words[0].charAt(0) + words[1].charAt(0) 
}