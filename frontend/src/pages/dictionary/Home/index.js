import React, {useState} from 'react'
import {Box, Typography, FilledInput, IconButton, Button} from '@material-ui/core'
import {Search as SearchIcon, Bookmark as BookmarkIcon} from '@material-ui/icons'
import image from '../../../assets/logo.jpg'
import {useHistory} from 'react-router-dom'


const Home = () => {
  const [word, setWord] = useState("")
  const history = useHistory()  

  const handleSubmit = (event) => {
    event.preventDefault()
    console.log('search word')
    const trimmedWord = word.trim();
    if (!trimmedWord || trimmedWord.split(" ").length > 1) return;
    history.push(`/search/${word}`)
  }
  
  return (
    <Box sx={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
    }}>
      <img src={image} alt="Book" width="250" />
      <Typography 
        color='primary'
        sx={{
          mt: 3,
          mb: 1
        }}
        variant='h4'
      >
        Inna Dictionary
      </Typography>
      <Typography>Azul, this is inna, manikantgit aywi ḥenna?</Typography>
      <Typography>inɣayi umarg-nnek</Typography>
      <Box sx={{
        width:'360px'
      }}>
        <form onSubmit={handleSubmit}>
        <FilledInput
          value={word}
          onChange={event => setWord(event.target.value)}
          sx={{
            my: 4,
            backgroundColor: 'white',
            borderRadius: 2,
            boxShadow: '0px 10px 25px rgba(0, 0, 0, 0.05)',
            '& .MuiFilledInput-input': {
              p: 2
            }
          }}
          placeholder='search word'
          startAdornment={<SearchIcon color='disabled'/> } 
          disableUnderline
          fullWidth 
        />
        </form>
      </Box>
      <IconButton sx={{
        backgroundColor: 'red',
        borderRadius: 2,
        p: 2,
        color: '#fff',
        backgroud: 'linear-gradient(138.72deg, #DC8295, 0%, #DC387C 95.83%)',
        boxShadow: '0px 10px 10px rgba(221, 114, 133, 0.2)',
      }}>
        <BookmarkIcon/>
      </IconButton>
    </Box>
  )
}

export default Home
