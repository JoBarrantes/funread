import { useState } from 'react'
import { useSelector } from 'react-redux'
import './BookBuilder.sass'
import { Radio } from 'antd'
import { Container, Row, Col, Form } from 'react-bootstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGlobe, faLock } from '@fortawesome/free-solid-svg-icons'
import { toast } from 'react-toastify'
import { save, upload } from '../../../api'
import { new_book } from '../../../api/books'
import BookImage from '../BookImage/BookImage'

const initialBookState = {
  title: '',
  category: 0,
  portrait: null,
  createdby: null,
  updatedby: null,
  state: 0,
  sharedbook: 0,
  lastupdateby: null,
  description: '',
}

const getImage = 'http://localhost:8000/Media/'

const defaultImage = '/imagenes/no-image.png'

const BookBuilder = ({ toggleSidebar }) => {
  const [book, setBook] = useState(initialBookState)
  const [fileImage, setFileImage] = useState(null)
  const [errorMessage, setErrorMessage] = useState('')
  const [errorFields, setErrorFields] = useState({})
  const formatFileImage = new FormData()
  formatFileImage.append('image', fileImage)
  const user = useSelector((state) => state.user)

  const handleChange = (e) => {
    const { name, value } = e.target
    setBook({ ...book, [name]: value })
  }

  const handleSharedBookChange = (e) => {
    setBook({ ...book, sharedbook: e.target.value })
  }

  const handleImageSelect = (selectedImage) => {
    setFileImage(selectedImage)
  }

  const updateBookPortrait = (fileName) => {
    setBook({ ...book, portrait: fileName })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    try {
      // Validar campos
      const isValid = validateForm()
      if (!isValid) {
        return
      }
      const imageRoute = book.portrait ? await uploadImage() : null

      // Crear libro con ruta de imagen
      const newBook = {
        ...book,
        portrait: imageRoute,
        createdby: user.userId,
        updatedby: user.userId,
        lastupdateby: user.userId,
      }

      // Enviar libro al servidor
      const response = await createBook(newBook)

      if (response.data && response.status === 201) {
        const { portrait } = response.data

        toast.success('Book created successfully')

        const imageToDisplay = portrait
          ? `${getImage}${portrait}` // Usar la imagen del servidor
          : defaultImage // Usar la imagen predeterminada local

        toggleSidebar({ ...newBook, portrait: imageToDisplay })
      } else {
        toast.error('Unable to save the book')
      }
    } catch (error) {
      toast.error(
        'Request Error: An error occurred while processing your request'
      )
    }
  }

  const validateForm = () => {
    const requiredFields = ['title', 'category']
    const missingFields = requiredFields.filter((field) => !book[field])

    if (missingFields.length > 0) {
      setErrorMessage('There are missing fields')

      const updatedErrorFields = {}
      requiredFields.forEach((field) => {
        if (!book[field]) {
          updatedErrorFields[field] = true
        }
      })

      setErrorFields(updatedErrorFields)

      return false
    }

    setErrorMessage('')
    setErrorFields({})
    return true
  }

  const uploadImage = async () => {
    const response1 = await uploadImageFile()

    if (!response1.data || !response1.data.name) {
      throw new Error('Error uploading the image')
    }

    const imageName = response1.data.name
    const response2 = await getImageRoute(imageName)

    if (!response2.data || !response2.data.image_route) {
      throw new Error('Error getting the image route')
    }

    return response2.data.image_route
  }

  const uploadImageFile = async () => {
    return await save(formatFileImage)
  }

  const getImageRoute = async (imageName) => {
    return await upload(imageName)
  }

  const createBook = async (newBook) => {
    return await new_book(
      newBook.title,
      newBook.category,
      newBook.portrait,
      newBook.createdby,
      newBook.updatedby,
      newBook.state,
      newBook.sharedbook,
      newBook.lastupdateby,
      newBook.description
    )
  }

  return (
    <Container>
      <Row>
        <Col>
          <Form onSubmit={handleSubmit}>
            <Radio.Group
              onChange={handleSharedBookChange}
              required
              value={book.sharedbook}
              style={{ marginTop: '50px', marginBottom: '30px' }}
            >
              <Radio.Button className='custom-radio-button-wrapper' value={1}>
                <FontAwesomeIcon icon={faGlobe} className='pe-2' />
                Public
              </Radio.Button>
              <Radio.Button className='custom-radio-button-wrapper' value={0}>
                <FontAwesomeIcon icon={faLock} className='pe-2' />
                Private
              </Radio.Button>
            </Radio.Group>

            <BookImage
              onImageSelect={handleImageSelect}
              updateBookPortrait={updateBookPortrait}
            />

            <Form.Control
              className={`custom-book-builder-form-title ${
                errorFields.title ? 'error-title' : ''
              }`}
              type='text'
              name='title'
              placeholder='Name of the book'
              value={book.title}
              onChange={handleChange}
            />

            <Form.Control
              className='custom-book-builder-text-area'
              as='textarea'
              placeholder='Description'
              rows={4}
              name='description'
              value={book.description}
              onChange={handleChange}
            />

            <Form.Control
              className={`custom-book-builder-select ${
                errorFields.category ? 'error' : ''
              }`}
              as='select'
              name='category'
              value={book.category}
              onChange={handleChange}
            >
              <option value=''>Class</option>
              <option value={1}>Fiction</option>
              <option value={2}>History</option>
              <option value={3}>Fantasy</option>
            </Form.Control>

            {errorMessage && <p className='error-message'>{errorMessage}</p>}
            <button className='custom-save-button' type='submit'>
              Save
            </button>
          </Form>
        </Col>
      </Row>
    </Container>
  )
}

export default BookBuilder
