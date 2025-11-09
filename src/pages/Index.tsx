import { FormCard } from "@/components/FormCard";

const Index = () => {
  return (
    <main className="min-h-screen flex items-center justify-center p-4 bg-gradient-to-br from-background via-background to-secondary/20">
      <div className="w-full max-w-6xl mx-auto">
        <div className="text-center mb-8 space-y-4">
          <h1 className="text-5xl font-bold tracking-tight">
            <span className="bg-gradient-to-r from-primary via-accent to-primary bg-clip-text text-transparent">
              Welcome
            </span>
          </h1>
          <p className="text-lg text-muted-foreground max-w-md mx-auto">
            Fill out the form below and your data will be sent to your Flask API
          </p>
        </div>
        
        <div className="flex justify-center">
          <FormCard />
        </div>
      </div>
    </main>
  );
};

export default Index;
