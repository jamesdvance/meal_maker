import { createClient } from '@supabase/supabase-js';

// Use a custom domain as the supabase URL
const supabase = createClient('https://my-custom-domain.com', 'public-anon-key')

